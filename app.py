from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    num1 = ''
    num2 = ''
    
    if request.method == 'POST':
        try:
            # Получаем числа из формы
            num1 = request.form.get('num1', '')
            num2 = request.form.get('num2', '')
            
            # Преобразуем в числа и складываем
            result = float(num1) + float(num2)
        except (ValueError, TypeError):
            result = "Ошибка: введите числа!"
    
    return render_template('calculator.html', result=result, num1=num1, num2=num2)

if __name__ == '__main__':
    app.run(debug=True)