from foldrm import *
from datasets import *
from timeit import default_timer as timer
from datetime import timedelta


def main():
 
    # model, data = exercise()
    # model, data = data_science()
    # model, data = air()

    data_train, data_test = split_data(data, ratio=0.8)

    start = timer()
    model.fit(data_train, ratio=0.5)
    end = timer()

    model.print_asp(simple=True)
    Y = [d[-1] for d in data_test]
    Y_test_hat = model.predict(data_test)
    acc = get_scores(Y_test_hat, data_test)
    print('% acc', round(acc, 4), '# rules', len(model.crs))
    acc, p, r, f1 = scores(Y_test_hat, Y, weighted=True)
    print('% acc', round(acc, 4), 'macro p r f1', round(p, 4), round(r, 4), round(f1, 4), '# rules', len(model.crs))
    print('% foldrm costs: ', timedelta(seconds=end - start), '\n')

    # k = 1
    # for i in range(len(data_test)):
    #     print('Explanation for example number', k, ':')
    #     print(model.explain(data_test[i]))
    #     print('Proof Tree for example number', k, ':')
    #     print(model.proof(data_test[i]))
    #     k += 1


if __name__ == '__main__':
    main()
