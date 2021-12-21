to_analyze = 'Goodread_Results (9.96hrs)/log.txt'
ndcg10_valid = []
hit10_valid = []
ndcg10_test = []
hit10_test = []
with open(to_analyze, 'r') as f:
    for idx, i in enumerate(f):
        i = i.replace(')', '')
        i = i.replace('\n', '')
        i = i.replace(' ', '')
        line = i.split('(')
        # print(line)


        split_val = line[1].split(',')
        ndcg10_valid.append(float(split_val[0]))
        hit10_valid.append(float(split_val[1]))
        # print(split_val)

        split_val = line[2].split(',')
        ndcg10_test.append(float(split_val[0]))
        hit10_test.append(float(split_val[1]))
        # print(split_val)

print('average ndcg@10_valid: %.4f' % (sum(ndcg10_valid) / len(ndcg10_valid)))
print('average hit@10_valid: %.4f' % (sum(hit10_valid) / len(hit10_valid)))
print('average ndcg@10_test: %.4f' % (sum(ndcg10_test) / len(ndcg10_test)))
print('average hit@10_test: %.4f' % (sum(hit10_test) / len(hit10_test)))
