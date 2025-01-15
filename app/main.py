from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
from app.functions import Registration

app = FastAPI()
reg = Registration()

router = APIRouter()


class Employeedetails(BaseModel):
    emp_id: str
    emp_name: str
    emp_designation: str 


@app.get("/")
def read_root():
    return {"Hello": "employee registration app"}


@app.post("/employee-registration")
async def employee_registration(employeedetails: Employeedetails):
    emp_dict = employeedetails.dict()
    message = reg.insert_employee(emp_dict)
    return message
