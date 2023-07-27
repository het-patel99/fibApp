from django.shortcuts import render, redirect
from .models import FibonacciNumber
from django.utils import timezone

def fibonacci_form(request):
    if request.method == 'POST':
        n = int(request.POST.get('n', 0))
        identifier = str(timezone.now().timestamp())
        FibonacciNumber.objects.filter(calculation_identifier=identifier).delete()
        fibonacci_numbers = calculate_fibonacci(n)
        save_fibonacci_numbers(fibonacci_numbers,identifier,n)
        return redirect('fibonacci_result', n=n, identifier=identifier)
    return render(request, 'fibonacci_form.html')

def calculate_fibonacci(n):
    fibonacci_numbers = []
    
    if n >= 1:
        fibonacci_numbers.append(0)
    if n >= 2:
        fibonacci_numbers.append(1)
    
    for i in range(2, n):
        next_fib = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_fib)
    
    return fibonacci_numbers

def save_fibonacci_numbers(numbers, identifier, input_number):
    fibonacci_sequence = ', '.join(str(num) for num in numbers)
    FibonacciNumber.objects.create(
        input_number=input_number,
        fibonacci_sequence=fibonacci_sequence,
        calculation_identifier=identifier
    )

def fibonacci_result(request, n, identifier):
    fibonacci_data = FibonacciNumber.objects.filter(input_number=n).first()
    if fibonacci_data:
        input_number = fibonacci_data.input_number
        fibonacci_sequence = fibonacci_data.fibonacci_sequence.split(', ')
    else:
        input_number = n
        fibonacci_sequence = calculate_fibonacci(n)
        fibonacci_sequence_str = ', '.join(str(num) for num in fibonacci_sequence)
        save_fibonacci_numbers(fibonacci_sequence, identifier, input_number)

    return render(request, 'fibonacci_result.html', {'input_number': input_number, 'fibonacci_sequence': fibonacci_sequence})