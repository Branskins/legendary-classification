from joblib import dump, load


def save_model(model, file):
    dump(model, file)


def recover_model(file):
    model = load(file)
    return model
