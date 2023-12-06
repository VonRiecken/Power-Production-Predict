from power_predict.logic.registry import load_model
from power_predict.params import PREDICTION_TARGETS

def load_target_model(target:str = None):
    if target not in PREDICTION_TARGETS:
        return 'Target not in scope'

    if target == 'Solar':
        model = load_model(best_solar)
    elif target == 'Hydro':
        model = load_model(best_hydro)
    elif target == 'Wind':
        model = load_model(best_wind)
    elif target == 'Total':
        model = load_model(best_total)
    else:
        model = load_model(best_total)

    return model

# Best Models
best_hydro = 'knn_4feats_log'
best_solar = 'KNN_Poly_4feats_TIME_log'
best_wind = 'KNN_Poly_4feats_TIME_log'
best_total = 'KNN_Poly_4feats_TIME_log'

def get_target_index(target: str) -> int:
    if target not in PREDICTION_TARGETS:
        return 'Target not in scope'

    if target == 'Hydro':
        return 0
    elif target == 'Solar':
        return 1
    elif target == 'Wind':
        return 2
    else:
        return 3
