from scenarios.health_check import HealthCheckUser
from scenarios.customer_crud import CustomerCRUDUser
from scenarios.calculate_price import CalculatePriceUser
from scenarios.get_all_customers import GetAllCustomersUser
from scenarios.magic_endpoint import MagicEndpointUser


user_classes = [
    HealthCheckUser,
    GetAllCustomersUser,
    MagicEndpointUser,
    CustomerCRUDUser,
    CalculatePriceUser,
]
