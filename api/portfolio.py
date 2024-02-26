from fastapi import Response, APIRouter
import redis

portfolio_router = APIRouter()


def get_redis():
    return redis.Redis(db=0)


@portfolio_router.get('/portfolio')
def get_portfolio_data():
    redis_obj = get_redis()
    data = redis_obj.get("about_me")
    if data:
        return Response(content=data, media_type="application/json")
    else:
        return Response(content='{"msg": "No Portfolio Data Found"}', media_type="application/json")





