import http.server
import socketserver
import json
import os

PORT = 8000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(BASE_DIR, "state.json")

def get_canonical_doc_id(title_or_fname):
    base = title_or_fname.strip()
    if base.lower().endswith(".md"):
        base = base[:-3]
    slug = "".join(c if (c.isalnum() or c in ("-", "_")) else "_" for c in base).strip("_").lower()
    return "doc_" + (slug if slug else "nuevo")

def get_safe_filename(title):
    clean = "".join(c for c in title if c.isalnum() or c in (" ", "-", "_", ".")).rstrip()
    if not clean.endswith(".md"):
        clean += ".md"
    return clean

def load_state():
    state = {}
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                state = json.load(f)
        except Exception:
            state = {}

    if not isinstance(state, dict):
        state = {}

    if "markdownDocs" not in state or not isinstance(state["markdownDocs"], dict):
        state["markdownDocs"] = {}

    # 1. Deduplicar y normalizar documentos Markdown existentes en el estado
    clean_docs = {}
    for k, v in list(state["markdownDocs"].items()):
        if not isinstance(v, dict):
            continue
        title = v.get("title", "").strip()
        if not title:
            continue
        canon_id = get_canonical_doc_id(title)

        found_key = None
        for ck, cv in clean_docs.items():
            if ck == canon_id or (cv.get("title", "").strip().lower() == title.lower()):
                found_key = ck
                break

        if found_key:
            prev = clean_docs[found_key]
            # Priorizar documento editado por usuario en lugar de Sistema
            if prev.get("updatedBy") == "Sistema" and v.get("updatedBy") != "Sistema":
                v["id"] = found_key
                clean_docs[found_key] = v
            elif len(v.get("content", "")) > len(prev.get("content", "")):
                v["id"] = found_key
                clean_docs[found_key] = v
        else:
            v["id"] = canon_id
            clean_docs[canon_id] = v

    state["markdownDocs"] = clean_docs

    # 2. Cargar y sincronizar documentos Markdown de docs/ sin duplicados
    docs_dir = os.path.join(BASE_DIR, "docs")
    if os.path.exists(docs_dir):
        for fname in sorted(os.listdir(docs_dir)):
            if fname.endswith(".md"):
                canon_id = get_canonical_doc_id(fname)
                already_exists = False
                for k, v in state["markdownDocs"].items():
                    if k == canon_id:
                        already_exists = True
                        break
                    if isinstance(v, dict):
                        v_title = v.get("title", "").strip()
                        if v_title.lower() == fname.lower() or get_safe_filename(v_title).lower() == fname.lower():
                            already_exists = True
                            break

                if not already_exists:
                    file_path = os.path.join(docs_dir, fname)
                    try:
                        with open(file_path, "r", encoding="utf-8") as f_md:
                            state["markdownDocs"][canon_id] = {
                                "id": canon_id,
                                "title": fname,
                                "content": f_md.read(),
                                "updatedBy": "Sistema",
                                "updatedAt": os.path.getmtime(file_path)
                            }
                    except Exception:
                        pass
    return state

def save_state(state):
    try:
        if os.path.exists(STATE_FILE) and os.path.getsize(STATE_FILE) > 500:
            import shutil
            shutil.copyfile(STATE_FILE, STATE_FILE + ".bak")
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("Error al guardar estado:", e)

class SyncHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def end_headers(self):
        # Desactivar cache para que los datos siempre estén al segundo
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Cache-Control")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()

    def do_GET(self):
        if self.path == "/api/state":
            state = load_state()
            data = json.dumps(state).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == "/api/state":
            try:
                length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(length)
                payload = json.loads(body.decode("utf-8"))

                state = load_state()

                if isinstance(payload, dict):
                    if payload.get("reset"):
                        # Solo desmarcar casillas booleanas, NUNCA borrar subtasks, notas, customTasks o customSections!
                        for k, v in list(state.items()):
                            if isinstance(v, bool):
                                state[k] = False
                    elif payload.get("action") == "update_subtasks":
                        item_id = str(payload.get("id", ""))
                        tasks = payload.get("tasks", [])
                        if "subtasks" not in state or not isinstance(state["subtasks"], dict):
                            state["subtasks"] = {}
                        state["subtasks"][item_id] = tasks
                    elif payload.get("action") == "update_item_status":
                        item_id = str(payload.get("id", ""))
                        status_data = payload.get("status", {})
                        if "itemStatus" not in state or not isinstance(state["itemStatus"], dict):
                            state["itemStatus"] = {}
                        state["itemStatus"][item_id] = status_data
                    elif payload.get("action") == "archive_item":
                        item_id = str(payload.get("id", ""))
                        archive_data = payload.get("data", {})
                        if "archived" not in state or not isinstance(state["archived"], dict):
                            state["archived"] = {}
                        state["archived"][item_id] = archive_data
                    elif payload.get("action") == "restore_item":
                        item_id = str(payload.get("id", ""))
                        if "archived" in state and isinstance(state["archived"], dict):
                            state["archived"].pop(item_id, None)
                    elif payload.get("action") == "update_order":
                        section_id = str(payload.get("sectionId", ""))
                        order_list = payload.get("order", [])
                        if "orders" not in state or not isinstance(state["orders"], dict):
                            state["orders"] = {}
                        state["orders"][section_id] = order_list
                    elif payload.get("action") == "update_section_order":
                        tab_key = str(payload.get("tab", ""))
                        order_list = payload.get("order", [])
                        if "sectionOrders" not in state or not isinstance(state["sectionOrders"], dict):
                            state["sectionOrders"] = {}
                        state["sectionOrders"][tab_key] = order_list
                    elif payload.get("action") == "add_custom_task":
                        task_id = str(payload.get("id", ""))
                        task_data = payload.get("data", {})
                        if "customTasks" not in state or not isinstance(state["customTasks"], dict):
                            state["customTasks"] = {}
                        state["customTasks"][task_id] = task_data
                    elif payload.get("action") == "add_custom_section":
                        sec_id = str(payload.get("id", ""))
                        sec_data = payload.get("data", {})
                        if "customSections" not in state or not isinstance(state["customSections"], dict):
                            state["customSections"] = {}
                        state["customSections"][sec_id] = sec_data
                    elif payload.get("action") == "delete_custom_section":
                        sec_id = str(payload.get("id", ""))
                        if "customSections" in state and isinstance(state["customSections"], dict):
                            state["customSections"].pop(sec_id, None)
                    elif payload.get("action") == "save_markdown_doc":
                        doc_id = str(payload.get("id", ""))
                        doc_data = payload.get("data", {})
                        if "markdownDocs" not in state or not isinstance(state["markdownDocs"], dict):
                            state["markdownDocs"] = {}

                        raw_title = doc_data.get("title", f"doc_{doc_id}").strip()
                        safe_name = get_safe_filename(raw_title)
                        canon_id = get_canonical_doc_id(raw_title)

                        # Preferir ID canónico
                        target_id = canon_id if (doc_id.startswith("doc_1") and "_" in doc_id) else (doc_id or canon_id)
                        doc_data["id"] = target_id

                        docs_dir = os.path.join(BASE_DIR, "docs")
                        os.makedirs(docs_dir, exist_ok=True)

                        # Si se renombró el título, limpiar el archivo con el nombre anterior
                        try:
                            old_doc = state["markdownDocs"].get(target_id) or state["markdownDocs"].get(doc_id)
                            if old_doc and isinstance(old_doc, dict):
                                old_title = old_doc.get("title", "").strip()
                                new_title = doc_data.get("title", "").strip()
                                if old_title and new_title and old_title != new_title:
                                    old_safe = get_safe_filename(old_title)
                                    old_path = os.path.join(docs_dir, old_safe)
                                    if os.path.exists(old_path):
                                        os.remove(old_path)
                        except Exception:
                            pass

                        # Eliminar cualquier duplicado previo por ID o por nombre de archivo/título
                        keys_to_remove = [
                            k for k, v in state["markdownDocs"].items()
                            if k != target_id and (
                                k == doc_id or
                                (isinstance(v, dict) and (
                                    v.get("title", "").strip().lower() == raw_title.lower() or
                                    get_safe_filename(v.get("title", "")).lower() == safe_name.lower()
                                ))
                            )
                        ]
                        for k in keys_to_remove:
                            state["markdownDocs"].pop(k, None)

                        state["markdownDocs"][target_id] = doc_data
                        # Guardar copia física en docs/miWork/docs/
                        try:
                            f_path = os.path.join(docs_dir, safe_name)
                            with open(f_path, "w", encoding="utf-8") as f_out:
                                f_out.write(doc_data.get("content", ""))
                        except Exception as e_md:
                            print("Error al sincronizar archivo .md en docs/:", e_md)
                    elif payload.get("action") == "delete_markdown_doc":
                        doc_id = str(payload.get("id", ""))
                        if "markdownDocs" in state and isinstance(state["markdownDocs"], dict):
                            removed = state["markdownDocs"].pop(doc_id, None)
                            raw_title = removed.get("title", "").strip() if (removed and isinstance(removed, dict)) else ""

                            # Si no se encontró por doc_id, buscar por título
                            if not raw_title:
                                for k, v in list(state["markdownDocs"].items()):
                                    if k == doc_id or (isinstance(v, dict) and v.get("id") == doc_id):
                                        raw_title = v.get("title", "").strip()
                                        state["markdownDocs"].pop(k, None)
                                        break

                            # Eliminar cualquier duplicado residual con el mismo título
                            if raw_title:
                                safe_name = get_safe_filename(raw_title)
                                for k in [k for k, v in state["markdownDocs"].items() if isinstance(v, dict) and (v.get("title", "").strip().lower() == raw_title.lower() or get_safe_filename(v.get("title", "")).lower() == safe_name.lower())]:
                                    state["markdownDocs"].pop(k, None)

                                try:
                                    docs_dir = os.path.join(BASE_DIR, "docs")
                                    f_path = os.path.join(docs_dir, safe_name)
                                    if os.path.exists(f_path):
                                        os.remove(f_path)
                                except Exception:
                                    pass
                    elif payload.get("action") == "sync_all":
                        if isinstance(payload.get("state"), dict):
                            state = payload["state"]
                    elif "id" in payload and "checked" in payload:
                        state[payload["id"]] = bool(payload.get("checked", False))
                    elif "id" in payload and "tasks" not in payload and "action" not in payload:
                        state[payload["id"]] = bool(payload.get("checked", False))
                    else:
                        state.update(payload)

                save_state(state)

                resp = json.dumps({"status": "ok", "state": state}, ensure_ascii=False).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(resp)))
                self.end_headers()
                self.wfile.write(resp)
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    print(f"Servidor colaborativo en tiempo real iniciado en el puerto {PORT}...")
    print(f"Directorio de trabajo: {BASE_DIR}")
    with ThreadedTCPServer(("", PORT), SyncHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor cerrado.")
