store = {}


def save_context(context_id, payload):
    store[context_id] = payload


def get_context(context_id):
    return store.get(context_id)