from pal import models


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        # if request.user.is_authenticated:
        # try:
        #     print(f"------------------------------------middleware {request.user}")
        # except:
        #     print("An exception occurred")
        # print(f"------------------------------------middleware {request.method}")
        # print(f"------------------------------------middleware {request.body}")
        # print(f"------------------------------------middleware {request.headers}")
        # print(f"------------------------------------middleware {request.get_host()}")
        # print(f"------------------------------------middleware {request.get_full_path()}")
        # print(f"------------------------------------middleware {request.build_absolute_uri()}")


        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        user = None
        try:
            user = str(request.user)
        except:
            print("user exception occurred")

        method = None
        try:
            method = request.method
        except:
            print("method exception occurred")

        body = None
        try:
            body = str(request.body)
        except:
            print("body exception occurred")

        header = None
        try:
            header = str(request.headers)
        except:
            print("header exception occurred")

        meta = None
        try:
            meta = str(request.META)
        except:
            print("META exception occurred")

        endpoint = None
        try:
            endpoint = str(request.endpoint)
        except:
            print("endpoint exception occurred")

        res = None
        try:
            res = str(response.content)
        except:
            print("response exception occurred")


        try:
            obj = models.AppRequest.objects.create(
                creator=user,
                method=method,
                body=body,
                header=header,
                endpoint=endpoint,
                response=res,
                meta=meta,
            )

            obj.save()
        except:
            print("response save exception occurred")



        # print(f"------------------------------------middleware {response.content}")
        # print(f"------------------------------------middleware {response.headers}")

        return response

    return middleware