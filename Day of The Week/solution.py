class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        from datetime import date
        days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        difference = date(year,month,day) - date(1971,1,1)
        return days_of_week[(difference.days + 5) % 7]
