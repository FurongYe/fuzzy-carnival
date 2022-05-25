def _simple_evaluate(integer_para, continous_para, categorical_para) :
    result = sum(integer_para) + sum(continous_para) + categorical_para.size()
    return result