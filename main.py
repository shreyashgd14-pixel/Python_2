from temperature.celsius import c_to_f, c_to_k
from temperature.fahrenhiet import f_to_c
from temperature.kelvin import k_to_c

def main():
    print("Temperature Conversion Options:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
      
    choice=int(input("Enter your choice (1/2/3): "))

    if choice==1:
        celsius=float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C={c_to_f(celsius)}°F")

    elif choice==2:
        Fahrenheit=float(input("Enter temperature in Fahrenh Fahrenheit")) 
        print(f"{Fahrenheit}°F={f_to_c(Fahrenheit)}°C")

    elif choice==3:
        celsius=float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C={c_to_k(celsius)}k")
    
    else:
        print("Invalid choice")

main()