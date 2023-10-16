from mylib.crud import (
    load,
    insert,
    read_record_id,
    update_record,
    delete_record,
    close_conn,
)


def main():
    load("diabetes.csv")
    insert(4, 94, 78, 31, 85, 33.1, 0.446, 22, 1)
    update_record(1, 4, 94, 78, 31, 85, 33.1, 0.446, 22, 1)
    read_record_id(3)
    delete_record(1)
    close_conn()
    return 0


if __name__ == "__main__":
    main()
