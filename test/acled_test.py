import acled


if __name__ == '__main__':

    df = acled.acled(key="key",
                     email="email@email.com",
                     year=2022)

    print(df)
