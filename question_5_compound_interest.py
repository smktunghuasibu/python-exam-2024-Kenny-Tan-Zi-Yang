# This program is used to calculate compound interest.
# User can input: 
# (a) principal (p), 
# (b) interest rate (r), 
# (c) time in years (t), and 
# (d) number of periods the interest is compounded per year (n)

def cal_matured_value(p, r, t, n):
    result = p * (1 + (r / 100) / n) ** (n * t)
    return result 

def get_inputs():
    p = float(input("Enter the principal amount: ")) 
    r = float(input("Enter the interest rate: ")) 
    t = float(input("Enter the time in years: ")) 
    n = float(input("Enter the number of periods the interest is compounded per year: ")) 
    return (p, r, t, n) 
    
def main():
    p, r, t, n = get_inputs()
    matured_value = cal_matured_value(p, r, t, n)
    print(f"Matured value is {matured_value:.2f}") 

# Don't change the code below!
if __name__ == "__main__":
    main()
