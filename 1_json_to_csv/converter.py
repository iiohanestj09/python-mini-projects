import json

if __name__ == '__main__':
    try:
        with open('input.json', 'r') as f:
            data = json.loads(f.read())
            
        output = ','.join([*data[0]])       #? *data[0] -> menguraikan elemen, karena data ini object, maka hasil uraian keys
        for obj in data:
            output += f'\n{obj["nama"]},{obj['umur']},{obj['tahunLahir']}'
            
        with open('output.csv', 'w') as f:
            f.write(output)
    except Exception as ex:
        print(f"Error {str(ex)}")