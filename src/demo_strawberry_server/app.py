import asyncio
from typing import AsyncIterator

from aiohttp import web
from strawberry.aiohttp.views import GraphQLView
from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL

import strawberry

total_finally_calls = 0
total_num_subscriptions = 0

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "world"

async def add_to_queue(q, number):
    for i in range(number):
        await q.put(i)


async def get_Value(id) -> AsyncIterator[int]:
    global total_finally_calls
    global total_num_subscriptions

    try:
        while True:
            yield 1
            await asyncio.sleep(0.05)
    finally:
        total_finally_calls += 1
        print("finally called for subscription id: "+str(id) + \
            " -> total finally calls: " + str(total_finally_calls) + \
            " /"+str(total_num_subscriptions))

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def getValue(self, id: strawberry.ID) -> int:
        global total_num_subscriptions
        total_num_subscriptions += 1
        print("Subscribing to id: "+str(id))
        return get_Value(id)

class MyGraphQLView(GraphQLView):
    async def get_context(self, request: web.Request, response: web.StreamResponse):
        return {"request": request, "response": response}

def main(args=None) -> None:
    schema = strawberry.Schema(query=Query, subscription=Subscription)

    view = MyGraphQLView(
        schema=schema,
        subscription_protocols=[GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL],
    )

    app = web.Application()
    app.router.add_route("*", "/ws", view)
    web.run_app(app)

if __name__ == "__main__":
    main()