def solution(m, musicinfos):
    answer, maximum = "(None)", 0
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#','b')
    for musicinfo in musicinfos:
        first, last, title, melody = musicinfo.split(',')
        first, last = first.split(':'), last.split(':')
        melody = melody.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#','b')
        time = (int(last[0])*60 + int(last[1])) - (int(first[0])*60 + int(first[1]))
        melody = melody * (time // len(melody)) + melody[:time%len(melody)]
        if m in melody and time > maximum:
            answer = title
            maximum = time
    return answer