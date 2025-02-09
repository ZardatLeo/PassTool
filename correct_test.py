from tqdm import tqdm
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gen_filename', type=str, default='result.txt', help='生成的口令文件', required=True)
    parser.add_argument('--test_filename', type=str, default='passlen8_test.txt', help='测试集文件', required=True)
    return parser.parse_args()

args = parse_args()

filename = args.gen_filename # 生成的口令文件
pass_set = set()
with open(filename, 'r', encoding = 'utf-8') as file:
    pwds = file.readlines()
    for i in tqdm(range(len(pwds)), desc = '正在处理输入...'): #去掉换行符
        pass_set.add(pwds[i])

test_set = {}
test_filename = args.test_filename #测试集文件
with open(test_filename, 'r', encoding = 'utf-8') as file:
    test_pwds = file.readlines()
    for i in tqdm(range(len(test_pwds)), desc = '正在处理测试集...'): #去掉换行符
        test_set[test_pwds[i]] = 1

print('生成口令重复率:', (len(pwds) - len(pass_set)) / len(pwds) * 100, '%')
print('有效猜测次数:', len(pass_set))
correct = 0
cnt = 0
node = [1e6, 1e7, 1e8]
nd_cnt = 0
for p in pass_set:
    cnt += 1
    if p in test_set:
        correct += 1
    if cnt == node[nd_cnt]:
        nd_cnt += 1
        print(f'{node[nd_cnt - 1]}准确数:', correct)
        print(f'{node[nd_cnt - 1]}准确率:', min(1, correct / len(test_set)) * 100, '%')

print('最终准确数:', correct)
print('最终准确率:', min(1, correct / len(test_set)) * 100, '%')