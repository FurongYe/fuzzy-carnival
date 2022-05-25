
from abc import ABC, abstractmethod
from typing import Callable, Any, Tuple

from Configurator.searchspace import SearchSpace

class base(ABC):
    def __init__(
        self,
        objective_func : Callable,
        search_space : SearchSpace,
        budget : int = 5000,


        ):
        self.objective_func_ = objective_func
        self.search_space_ = search_space
        self.budget_ = budget
        
        self.configurations_ : list = []
        self.survivors_ : list = []
        self.elites_ : list =  []
        
    @property()
    def configurations(self) :
        return self.configurations_

    @property()
    def survivors(self) :
        return self.survivors_

    @property()
    def elites(self) :
        return self.elites_


    @abstractmethod    
    def set_parameters_() :
        return 

    @abstractmethod
    def generation():
        raise NotImplementedError

    def results():
        return self.elites_
