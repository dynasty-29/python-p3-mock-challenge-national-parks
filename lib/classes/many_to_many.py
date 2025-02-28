class NationalPark:
    all_parks = []
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 character long")
        self._name = name
        NationalPark.all_parks.append(self)
        
    # NationalPark property name
    # Returns the national_park's name        
    @property
    def name(self):
        return self._name    
    
    # Names must be of type str
    # Names length must be greater or equal to 3 characters
    # Should not be able to change after the national_park is instantiated    
    @name.setter
    def name(self, new_name):
        if hasattr(self, 'name'):
            raise ValueError("Name cannot be changes after initialization")
        if not isinstance(new_name, str):
            return ValueError("Name must be a string")
        if len(new_name) < 3:
            raise ValueError("Name must be at least 3 character long")
        self._name = new_name
        
    # Returns a list of all trips at a particular national park
    # Trips must be of type Trip       
    def trips(self):
        return [trip for trip in Trip.all_trips if trip.national_park == self]
    
    # Returns a unique list of all visitors a particular national park has welcomed
    # Visitors must be of type Visitor    
    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))
    
    # Returns the total number of times a park has been visited
    # Returns 0 if the park has no visits    
    def total_visits(self):
        return len(self.trips())

    # Returns the Visitor instance that has visited that park the most
    # Returns None if the park has no visitors 
    def best_visitor(self):
        if not self.visitors():
            return None
        
        visitor_counts = {}
        for visitor in self.visitors():
            visitor_counts[visitor] = visitor.total_visits_at_park(self)
            
        best_visitor = max(visitor_counts.items(), key=lambda x:x[1])[0]
        return best_visitor    

    # Returns the NationalPark instance with the most visits.
    # Returns None if there are no visits.
    # hint: will need a way to remember all NationalPark objects
    # hint: do you have a method to get the total visits for a particular NationalPark object?
    @classmethod
    def most_visited(cls):
        if not cls.all_parks:
            return None
        park_with_most_visits = max(cls.all_parks, key=lambda park: park.total_visits())
        
        if park_with_most_visits.total_visits() == 0:
            return None
        
        return park_with_most_visits

class Trip:
    all_trips = []
    
    # Trip __init__(self, visitor, national_park, start_date, end_date)
    # Trip is initialized with a Visitor instance, a NationalPark instance, a start_date, and an end_date
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all_trips.append(self)

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, new_visitor):
        if not isinstance(new_visitor, Visitor):
            raise ValueError("Visitor must be of type visitor")
        self._visitor = new_visitor
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, new_park):
        if not isinstance(new_park, NationalPark):
            raise ValueError("National Park must be of type NationalPark")
        self._national_park = new_park
        
    # Trip property start_date
    # Returns the trip's start_date
    # Start_date must be of type str
    # Start_date length must be greater or equal to 7 characters
    # Is in the format "September 1st"
    # Should be able to change after the trip is instantiated
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, new_date):
        if not isinstance(new_date, str):
            raise ValueError("Start date must be a string")
        if len(new_date) < 7:
            raise ValueError("Start date must be at least 7 characters long")
        self._start_date = new_date
        
    # Trip property end_date
    # Returns the trip's end_date
    # End_date must be of type str
    # End_date length must be greater or equal to 7 characters
    # Is in the format "September 1st"
    # Should be able to change after the trip is instantiated
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, new_end):
        if not isinstance(new_end, str):
            raise ValueError("End date must be a string")
        if len(new_end) < 7:
            raise ValueError("End date must be at least 7 character long")
        self._end_date = new_end
    
class Visitor:

    def __init__(self, name):
        self.name = name
        
    # Visitor property name
    # Returns the visitor's name        
    @property
    def name(self):
        return self.name  
    # Names must be of type str
    # Names must be between 1 and 15 characters, inclusive
    # Should be able to change after the visitor is instantiated
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) or not (1<= len(new_name) <= 15):
            return ValueError("Name must be a string and between 1 and 15 characters, inclusive")
        self._name = new_name  
        
    # Returns a list of all trips for that visitor
    # Trips must be of type Trip        
    def trips(self):
        return [trip for trip in Trip.all_trips if trip.visitor == self]
    
    # Returns a unique list of all parks that visitor has visited
    # Parks must be of type NationalPark
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))
    
    # Receives a NationalPark object as argument
    # Returns the total number of times a visitor visited the park passed in as argument
    # Returns 0 if the visitor has never visited the park    
    def total_visits_at_park(self, park):
        if not isinstance(park, NationalPark):
            raise ValueError("Park must be a type NationalPark")
        
        return len([trip for trip in self.trips() if trip.national_park== park])