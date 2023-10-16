from mylib.crud import (
    load,
    insert,
    read_record_id,
    update_record,
    delete_record,
    close_conn,
)
import argparse
from ast import literal_eval


def main():
    load("diabetes.csv")
    insert(4, 94, 78, 31, 85, 33.1, 0.446, 22, 1)
    update_record(1, 4, 94, 78, 31, 85, 33.1, 0.446, 22, 1)
    read_record_id(3)
    delete_record(1)
    close_conn()
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command Line Tool for SQLite")
    parser.add_argument(
        "operation", help="specify operation to perform: load|insert|delete|update|read"
    )
    parser.add_argument(
        "-a",
        "--argument",
        help="operation argument. For insert, provide a tuple (1,2,3...); for delete and read, provide an id; for update, provide a tuple (1,2,3...) with the first element being id",
    )
    args = parser.parse_args()
    op = args.operation
    op_arg = args.argument

    try:
        if op == "load":
            load()

        elif op == "insert" and op_arg:
            tup = literal_eval(op_arg)
            insert(*tup)
        elif op == "delete" and op_arg:
            delete_record(int(op_arg))
        elif op == "update" and op_arg:
            tup = literal_eval(op_arg)
            update_record(*tup)
        elif op == "read" and op_arg:
            read_record_id(int(op_arg))
        else:
            print(
                "Likely you have invalid argument, see the following instruction for help: \n"
            )
            parser.print_help()
    except TypeError as e:
        print("Likely your input to update or insert is ill-formated. Please check.\n")
        parser.print_help()

    close_conn()
