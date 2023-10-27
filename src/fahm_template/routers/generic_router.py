from fastapi import status, Body, APIRouter, Depends, Request
from fastapi.responses import Response, HTMLResponse
from fahm_template import MONGODB_URL, get_templates
from fastapi.templating import Jinja2Templates

PREFIX = ""

router = APIRouter()


@router.get("/", response_description="Just a hello world")
async def index(request: Request, templates: Jinja2Templates = Depends(get_templates)):
    return templates.TemplateResponse("index.html", context={'request': request, 'name': "Jeff"})
