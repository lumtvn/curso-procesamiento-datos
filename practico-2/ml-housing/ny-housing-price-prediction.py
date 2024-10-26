# import ....

from src.cross_validation import cross_validation
from src.feature_selection import feature_selection
from src.preprocessing import preprocessing
from src.training import training


if __name__ == '__main__':
    # ejecutar las distintas etapas del pipeline. Cuidar que cada etapa reciba y devuelva lo necesario para la siguiente.