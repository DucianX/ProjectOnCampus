def caculate_time_to_consume(total_gallons, pump_minutes):
    # Caculate how soon will the pump accmulate certain amount of water
    GOAL = 5
    switch = True
    if total_gallons >= GOAL and switch:  # Once we reach five gallon, we quit
        five_gallon = pump_minutes
        switch = False
        return five_gallon


def caculator_and_printer(data):
    pump_running = False
    pump_minutes = 0
    total_gallons = 0
    total_power_watt_minutes = 0
    recorder_length = []  # record the info of softener duration
    recorder_start = []  # record the start of softener

    for minute in data:
        watt_draw = int(minute)
        NOISE_CANCELLER = 500  # To cancel the noise
        if watt_draw > NOISE_CANCELLER:
            if not pump_running:
                pump_running = True
                start_index = data.index(minute)
                # Record the start of the water softener
        elif watt_draw <= NOISE_CANCELLER:
            if pump_running:
                pump_running = False
                stop_index = data.index(minute)
                # Record the stop of the water softener
                softener_duration = int(stop_index - start_index)
                if softener_duration > 120:
                    recorder_length.append(softener_duration)
                    recorder_start.append(start_index)
                    start_index = 0
                    stop_index = 0
                # watt<=500 means pump is turned off

        if pump_running:  # While pump is working, acummulate the data needed
            pump_minutes += 1
            total_power_watt_minutes += watt_draw
            total_gallons += 2
        caculate_time_to_consume(total_gallons, pump_minutes)

    five_gallon = caculate_time_to_consume(total_gallons, pump_minutes)
    total_minutes = len(data)
    total_hours = total_minutes / 60
    total_days = total_hours / 24
    duration_hours = float(pump_minutes / 60)  # pumping duration
    duration_days = float(duration_hours / 24)
    avg_consume_daily = total_gallons / total_days
    total_power_kwh = total_power_watt_minutes / (60 * 1000)
    print(f"Data covers a total of {round(total_hours, 3)} hours")
    print(f"(That's {round(total_days, 3)} days)\n")
    print(f"Pump was running for {pump_minutes} minutes, producing {total_gallons} gallons")
    print(f"(That's {round(avg_consume_daily, 3)} gallons per day)\n")
    print(f"Pump required a total of {total_power_watt_minutes} watt minutes of power")
    print(f"That's {round(total_power_kwh, 3)} kWh\n")
    print(f"It took {five_gallon} minutes of data to reach 5 gallons.")
    print("Information on water softener recharges:")
    print(f"{len(recorder_length)}")
    for i in range(len(recorder_length)):
        print(f"{recorder_length[i]} minute run started at {recorder_start[i]}")
        # WHY is it not WORKING????

def main():
    file_name = input("Please input the filename: ")

    try:
        with open(file_name, 'r') as file:
            data = file.read()
            data = data.splitlines()
            caculator_and_printer(data)
            # splitlines() makes the data a list.
    except FileNotFoundError:
        print(f"Unable to open {file_name}")


if __name__ == "__main__":
    main()
