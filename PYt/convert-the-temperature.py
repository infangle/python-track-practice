class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        ans =[]
        kelvin = celsius + 273.15000
        Fahrenheit = celsius * 1.80 + 32.00000
        ans = [kelvin, Fahrenheit]
        return ans
