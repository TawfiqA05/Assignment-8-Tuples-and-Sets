def states_with_high_test_results(input_file, output_file, threshold):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    header = lines[0].strip().split(',')
    date_index = header.index('date')
    state_index = header.index('state')
    total_test_results_index = header.index('totalTestResults')

    monthly_states = {}

    for line in lines[1:]:
        columns = line.strip().split(',')
        date = columns[date_index]
        state = columns[state_index]
        total_test_results = columns[total_test_results_index]

        if total_test_results.isdigit():
            total_test_results = int(total_test_results)
            if total_test_results > threshold:
                month = date[:6]  # Extract YYYYMM from date
                if month not in monthly_states:
                    monthly_states[month] = []
                monthly_states[month].append(state)

    with open(output_file, 'w') as file:
        file.write('month,states\n')
        for month, states in monthly_states.items():
            states_str = ';'.join(states)
            file.write(f'{month},{states_str}\n')

# Example usage
file_path = "/Users/tawfiqabulail/Downloads/Information Infrastructure I /covid_data_set.csv"
states_with_high_test_results(file_path, 'states_with_high_test_results.csv', 1000000)