from fastapi import Request

def items_common_logger(request: Request):
    print(f"[items_common_logger] {request.method} {request.url.path} request received")

def get_items_logger(request: Request):
    print(f"[get_items_logger] Fetching items...")
