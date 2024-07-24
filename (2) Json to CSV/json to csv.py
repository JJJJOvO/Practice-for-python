
import simplejson

if __name__ == '__main__':
    try:
        with open('input.json', 'r') as f:
            data = simplejson.loads(f.read())

        print(data)
        print(data[0])
        print(*(data[0].keys())) 
        # 获取字典键的方法：（1）dict.keys(): 返回一个字典键的迭代器 （2）*dict（**dict: 值）
        
        output = ','.join([*data[0]])
    
        for obj in data:
            output += f'\n{obj["Name"]},{obj["Age"]},{obj["Sex"]}'

        print(output)
        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f'Error: {str(ex)}')