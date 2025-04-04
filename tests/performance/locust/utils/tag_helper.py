from locust import tag


def tag_all_tasks(*tag_names):
    def decorator(cls):
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if callable(attr) and getattr(attr, "locust_task_weight", None) is not None:
                setattr(cls, attr_name, tag(*tag_names)(attr))
        return cls

    return decorator
