class TemperatureTracker:
    def __init__(self, company_name, company_address):
        self.company_name = company_name
        self.company_address = company_address
        self.num_days = 0
        self.temperature_readings = []
        self.temperature_categories = {'very_hot': 0, 'pleasant': 0, 'very_cold': 0}
        
    def input_temperature(self):
        self.num_days = int(input('How many days to record? '))
        print(f'\nEnter temperature readings for each day ({self.company_name}):')
        for i in range(self.num_days):
            temperature = int(input(f'Temperature day [{i+1}] = '))
            self.temperature_readings.append(temperature)

    def categorize_temperature(self, temp):
        if temp >= 85:
            return 'very_hot'
        elif temp >= 60:
            return 'pleasant'
        else:
            return 'very_cold'

    def display_information(self):
        print(f'\nDaily Temperatures Report for {self.company_name}:')
        for i, temp in enumerate(self.temperature_readings):
            category = self.categorize_temperature(temp)
            print(f'Temperature day [{i+1}] = {temp}°C ({category})')
        average_temperature = sum(self.temperature_readings) / self.num_days
        print(f'Average Temperature over {self.num_days} days = {average_temperature:.2f}°C')

    def final_display(self):
        print(f'\nNumber of very hot days = {self.temperature_categories["very_hot"]}')
        print(f'Number of pleasant days = {self.temperature_categories["pleasant"]}')
        print(f'Number of very cold days = {self.temperature_categories["very_cold"]}')


# Functional call
company_name = 'UniCampus'
company_address = 'Kathmandu Nepal'
tt = TemperatureTracker(company_name, company_address)
tt.input_temperature()
tt.display_information()
tt.final_display()
 