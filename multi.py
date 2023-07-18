import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"sleeping {seconds} second....")
    time.sleep(seconds)
    return f"done sleeping...{seconds}"


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} secons(s)")


if __name__ == "__main__":
    main()
