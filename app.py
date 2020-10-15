from flask import Flask

app = Flask(__name__)

@app.route("/<int:number>", methods = ["GET"])
def show_all(number):
    nums = " ".join([str(num) for num in range(1, number + 1)])
    return nums

@app.route("/<int:number>/odd", methods = ["GET"])
def show_odd(number):
    nums = " ".join([str(num) for num in range(1, number + 1, 2)])
    return nums

@app.route("/<int:number>/even", methods = ["GET"])
def show_even(number):
    nums = " ".join([str(num) for num in range(2, number + 1, 2)])
    return nums

@app.route("/<int:number>/prime", methods = ["GET"])
def show_prime(number):
    prime_nums = []
    sieve = [True] * (number + 1)
    for i in range(2, number + 1):
        if sieve[i]:
            prime_nums.append(str(i))
            for j in range(i, number + 1, i):
                sieve[j] = False
    return " ".join(prime_nums)

if __name__ == "__main__":
    app.run()