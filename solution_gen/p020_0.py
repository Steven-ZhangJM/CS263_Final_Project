

def main():
    num_counted = 1

    while True:
        num_fact_saved = 0
        total = 0
        num_fact = 0

        if (num_fact == num_counted):
            break

        while (num_fact % 10!= 0) and (num_fact_saved!= num_counted):
            num_fact = num_fact * 10 + (num_fact % 10)
            num_fact_saved += 1

        total += num_fact % 10
        num_counted = num_fact_saved

    print(total)

if __name__ == "__main__":
    main()

