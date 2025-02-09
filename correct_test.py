from tqdm import tqdm

filename = 'result.txt' # 生成的口令文件
pass_set = set()
with open(filename, 'r', encoding = 'utf-8') as file:
    pwds = file.readlines()
    for i in tqdm(range(len(pwds)), desc = '正在处理输入...'): #去掉换行符
        pass_set.add(pwds[i])

test_set = {}
test_filename = "passlen8_test.txt"      #测试集文件
with open(test_filename, 'r', encoding = 'utf-8') as file:
    test_pwds = file.readlines()
    for i in tqdm(range(len(test_pwds)), desc = '正在处理测试集...'): #去掉换行符
        test_set[test_pwds[i]] = 1

print('生成口令重复率:', (len(pwds) - len(pass_set)) / len(pwds) * 100, '%')
print('有效猜测次数:', len(pass_set))
correct = 0
cnt = 0
node = [1e5, 1e6, 1e7, 1e8]
for p in tqdm(pass_set, desc = '进度'):
    cnt += 1
    if p in test_set:
        correct += 1
    if cnt == 1e5:
        print('1e5准确数:', correct)
        print('1e5准确率:', min(1, correct / len(test_set)) * 100, '%')
    if cnt == 1e6:
        print('1e6准确数:', correct)
        print('1e6准确率:', min(1, correct / len(test_set)) * 100, '%')
    if cnt == 1e7:
        print('1e7准确数:', correct)
        print('1e7准确率:', min(1, correct / len(test_set)) * 100, '%')

print('最终准确数:', correct)
print('最终准确率:', min(1, correct / len(test_set)) * 100, '%')