import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.home.indexviewmodel import IndexViewModel
from viewmodels.shared.viewmodel import ViewModelBase

router = fastapi.APIRouter()


@router.get('/test')
@template()
def index(request: Request):
    print('This is Test View')
    vm = IndexViewModel(request)
    return vm.to_dict()



