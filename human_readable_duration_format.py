# Your task in order to complete this Kata is to write a function 
# which formats a duration, given as a number of seconds, in a 
# human-friendly way.

# The function must accept a non-negative integer. If it is zero, 
# it just returns "now". Otherwise, the duration is expressed as a 
# combination of years, days, hours, minutes and seconds.

def format_duration(seconds):
    if seconds != 0:
        y_d_h_m_s = dict()
        remaining_seconds = seconds % 60
        mins = (seconds - remaining_seconds) / 60
        remaining_mins = mins % 60
        hrs = (mins - remaining_mins) / 60
        remaining_hrs = hrs % 24
        days = (hrs - remaining_hrs) / 24
        remaining_days = days % 365
        years = (days - remaining_days) / 365
        y_d_h_m_s['year'] = int(years)
        y_d_h_m_s['day'] = int(remaining_days)
        y_d_h_m_s['hour'] = int(remaining_hrs)
        y_d_h_m_s['minute'] = int(remaining_mins)
        y_d_h_m_s['second'] = int(remaining_seconds)
        sentence_contructor = []
        for k, v in y_d_h_m_s.items():
            if v != 0:
                if v > 1:
                    sentence_contructor.append(f'{str(v)} {k}s')
                else:
                    sentence_contructor.append(f'{str(v)} {k}')
        sentence_list = [each for each in ', '.join(sentence_contructor)]
        sentence_list.reverse()
        if ',' in sentence_list:
            sentence_list[sentence_list.index(',')] = ' and'
        sentence_list.reverse()
        return ''.join(sentence_list)
    else:
        return 'now'

print(format_duration(1000000000000)) 
