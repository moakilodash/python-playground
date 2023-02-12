MUSIC_FILE = "Music.dat"
USERS_FILE = "Users.dat"


def user_input(input_str):
    return input_str.split(",")[0], input_str.split(" ")[-2]


def main():
    with open(MUSIC_FILE) as f:
        musics = dict()
        while True:
            line = f.readline().strip().split(";")
            if line == ['']:
                break
            musics[line[0]] = \
                [i.strip() for i in line
                 if i != line[0] and i != line[1]]

    with open(USERS_FILE) as f:
        users = dict()
        while True:
            line = f.readline().strip().split(";")
            if line == ['']:
                break
            users[line[0]] = \
                [i.strip() for i in line
                 if i != line[0]]

    u_name, n_songs = user_input(input("User name and surname, number of songs: "))

    output_genre1 = list()
    output_genre2 = list()

    for music in musics:
        if users[u_name][0] in musics[music]:
            output_genre1.append(music)
        output_genre1.sort()
        if users[u_name][1] in musics[music]:
            output_genre2.append(music)
        output_genre2.sort()

    for i in output_genre1:
        if i in output_genre2:
            output_genre2.remove(i)

    output = [*output_genre1, *output_genre2]

    for i, song in enumerate(output):
        if i >= int(n_songs):
            break
        print(f"   - {song}")


if __name__ == "__main__":
    main()
