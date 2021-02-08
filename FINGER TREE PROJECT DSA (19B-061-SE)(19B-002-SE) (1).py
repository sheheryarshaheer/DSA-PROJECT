#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections.abc import Sequence

class TREE__error(Exception):
    pass


class TreeIsVacant(TREE__error):
    """ 

Special case raised from inside Vacant when things like get_elemental or 

absentElemental are approached it. 

"""
    def __str__(self):
        return 


class Identity(object):
    pass


IDENTITY = Identity()


class Measure(object):
   

    def transmute(self, value):
        raise NotImplementedError
    
    def Operator(self, z, x):
        raise NotImplementedError
    

class convention__Count(Measure):
    
    def __init__(self, transmute, Operator, identity):
        self.transmute = transmute
        self.Operator = Operator
        self.identity = identity
    
    def __repr__(self):
        return (self.transmute, self.Operator, self.identity)


class EvaluateItem_count(Measure):
    def __init__(self):
        Measure.__init__(self)
        self.identity = 0
    
    def transmute(self, value):
        return 1
    
    def Operator(self, z, x):
        return a + b


class EvaluateWith__fingering(Measure):
    
    def __init__(self):
        Measure.__init__(self)
        self.identity = IDENTITY
    
    def Operator(self, z, x):
        if a is IDENTITY:
            return b
        elif b is IDENTITY:
            return a
        else:
            return self.SemiSort_Operator(z, x)
    
    def SemiSort_Operator(self, z, x):
        raise NotImplementedError

    
class MeasureLastItem(EvaluateWith__fingering):
    
    def transmute(self, value):
        return value
    
    def SemiSort_Operator(self, z, x):
        return b


class QuantifyMinMax(EvaluateWith__fingering):
    def transmute(self, value):
        return value
    
    def Operator(self, z, x):
            z_min, z_max = z
            x_min, x_max = x
            return min(z_min, x_min), max(z_max, x_max)


class Interpret_compute(Measure):
    
    def __init__(self, function, measure):
        Measure.__init__(self)
        self._function = function
        self._wrapped_transmute = measure.transmute
        self.Operator = measure.Operator
        self.identity = measure.identity
    
    def transmute(self, value):
        return self._wrapped_transmute(self._function(value))


class CombinedAssess(Measure):
    
    def __init__(self, *measures, **kwargs):
        self.measures = measures
        if "TupleClass" in kwargs:
            TupleClass = kwargs["tuple_class"]
            
            if hasattr(tuple_class, "_make"):
                self._MakeTuple = TupleClass._make

            else:
                self._MakeTuple = TupleClass
        else:
            self._MakeTuple = tuple
        self.identity = self._MakeTuple(m.identity for m in self.measures)
    
    def transmute(self, value):
        return self._MakeTuple(m.transmute(value) for m in self.measures)
    
    def Operator(self, z_values, x_values):
        return self._MakeTuple(m.Operator(z, x) for (m, z, x) in zip(self.measures, z_values, x_values))


class _VertexMeasure(Measure):
    def __init__(self, measure):
        self.transmute = self.transmute
        self.Operator = measure.Operator
        self.identity = measure.identity
    
    def transmute(self, Interchange):
        return Interchange.explanation


MEASURE_ITEM_COUNT = EvaluateItem_count()


class Interchange(Sequence):
    __slots__ = ["_values", "evaluate", "explanation"]
    def __init__(self, evaluate, *values):
        if len(values) not in (2, 3):
            raise Exception
        self._values = values
        self.evaluate = evaluate
        self.explanation = reduce(evaluate.Operator, map(evaluate.transmute, values))
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return Interchange(self.measure, *self._values[index])
        else:
            return self._values[index]
    
    def __len__(self):
        return len(self._values)
    
    def __add__(self, other):
        return Interchange(self.measure, *self._values + other._values)
    
    def __repr__(self):
        return .join([repr(v) for v in self])


class Digit(Sequence):
    __slots__ = ["_values", "evaluate", "explanation"]
    def __init__(self, measure, *values):
        if len(values) not in (1, 2, 3, 4):
            raise Exception % list(values)
        self._values = values
        self.evaluate = evaluate
        self.explanation = reduce(evaluate.Operator, map(evaluate.transmute, values))
    
    def Splitting_Digit(self, initial_explanation, predicate):
        split_point = 0
        while split_point < len(self):
            current_explanation = self.measure.Operator(initial_explanation, self.measure.transmute(self[split_point]))
            if predicate(current_explanation):
                break
            else:
                split_point += 1
                initial_explanation = current_explanation
        return self._values[:split_point], self._values[split_point:]
    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return Digit(self.measure, *self._values[index])
        else:
            return self._values[index]
    
    def __len__(self):
        return len(self._values)
    
    def __add__(self, other):
        return Digit(self.measure, *self._values + other._values)
    
    def __repr__(self):
        return "<Digit: %s>" % ", ".join([repr(v) for v in self])




class Tree(object):
   
    def Splitting(self, predicate):
        return self.Splitting_with(predicate, self.measure.identity)
    
    def __add__(self, other):
        if not isinstance(other, Tree):
            return NotImplemented
        return self.append(other)
    
    def __radd__(self, other):
        if not isinstance(other, Tree):
            return NotImplemented
        return self.prepend(other)


def to_tree(measure, sequence):
    tree = Vacant(measure)
    for value in sequence:
        tree = tree.affix_last(value)
    return tree


class Vacant(Tree):
    is_Vacant = True
    
    def __init__(self, measure):
        self.measure = measure
        self.explanation = measure.identity
    
    def get_elemental(self):
        raise TreeIsVacant
    
    def absentElemental(self):
        raise TreeIsVacant
    
    def PrependFirst(self, item):
        return Single(self.measure, item)
    
    def GetFinal(self):
        raise TreeIsVacant
    
    def WithoutPrior(self):
        raise TreeIsVacant
    
    def affix_last(self, item):
        return Single(self.measure, item)
    
    def prepend(self, other):
        return other
    
    def append(self, other):
        return other
    
    def iterate_values(self):
        if False:
            yield None
    
    def Splitting_with(self, predicate, initial_explanation):
        return self, self
    
    def __repr__(self):
        return "<Vacant>"


class Solitary(Tree):
    is_Vacant = False
    
    def __init__(self, measure, item):
        self.measure = measure
        self.explanation = measure.transmute(item)
        self.item = item
    
    def get_elemental(self):
        return self.item
    
    def absentElemental(self):
        return Vacant(self.measure)
    
    def PrependFirst(self, new_item):
        return Deep(self.measure, Digit(self.measure, new_item), Vacant(_VertexMeasure(self.measure)), Digit(self.measure, self.item))
    
    def GetFinal(self):
        return self.item
    
    def WithoutPrior(self):
        return Vacant(self.measure)
    
    def affix_last(self, new_item):
        return Deep(self.measure, Digit(self.measure, self.item), Vacant(_VertexMeasure(self.measure)), Digit(self.measure, new_item))
    
    def prepend(self, other):
        return other.affix_last(self.item)
    
    def append(self, other):
        return other.add_first(self.item)
    
    def iterate_values(self):
        yield self.item
    
    def Splitting_with(self, predicate, initial_explanation):
        if predicate(self.measure.Operator(initial_explanation, self.explanation)):
            return Vacant(self.measure), self
        else:
            return self, Vacant(self.measure)
    
    def __repr__(self):
        return "<Single: %r>" % (self.item,)


def ExtensiveLeft(measure, maybe_left, quill, right):
    """ 

Same as Deep(measure, maybe_left, quill, right), then again, actually maybe_left can 

be a rundown and is allowed to contain no things by any means. In such a case, a 

Exchange will be flown off of the plume and utilized as the left digit, with 

to_tree(right) being returned if the plume is really Vacant. 

"""
    if not maybe_left:
        if quill.is_Vacant:
            return to_tree(measure, right)
        else:
            return Deep(measure, Digit(measure, *quill.get_elemental()), quill.absentElemental(), right)
    else:
        return Deep(measure, Digit(measure, *maybe_left), quill, right)


def ExtensiveRight(measure, left, quill, maybe_right):
    """ 

Balanced activity to ExtensiveLeft that permits its correct digit to be a rundown 

that is conceivably Vacant. 

"""
    if not maybe_right:
        if quill.is_Vacant:
            return to_tree(measure, left)
        else:
            return Deep(measure, left, quill.WithoutPrior(), Digit(measure, *quill.GetFinal()))
    else:
        return Deep(measure, left, quill, Digit(measure, *maybe_right))


class Immeasurable(Tree):
    is_Vacant = False
    
    def __init__(self, measure, left, quill, right):
        self.measure = measure
        self.explanation = measure.Operator(measure.Operator(left.explanation, quill.explanation), right.explanation)
        self.left = left
        self.quill = quill
        self.right = right
    
    def get_elemental(self):
        """ 

Returns this current tree's first worth. 

Time multifaceted complexity: O(1). 

"""
        return self.left[0]
    
    def absentElemental(self):
        """ 

Returns another Tree occurrence addressing this tree with its first thing 

eliminated. 

Time multifaceted complexity: amortized O(1). 

"""
       
        if len(self.left) > 1:
            return Deep(self.measure, self.left[1:], self.quill, self.right)
        
        elif not self.quill.is_Vacant:
            return Deep(self.measure, Digit(self.measure, *self.quill.get_elemental()), self.quill.absentElemental(), self.right)
        
        elif len(self.right) == 1:
            return Single(self.measure, self.right[0])
        
        else:
            return Deep(self.measure, self.right[0:1], self.quill, self.right[1:])
    
    def PrependFirst(self, new_item):
       
        if len(self.left) < 4:
            return Deep(self.measure, Digit(self.measure, new_item) + self.left, self.quill, self.right)
        
        else:
            Interchange = Interchange(self.measure, self.left[1], self.left[2], self.left[3])
            return Deep(self.measure, Digit(self.measure, new_item, self.left[0]), self.quill.add_first(Interchange), self.right)
    
   
    
    def GetFinal(self):
        return self.right[-1]
    
    def WithoutPrior(self):
        if len(self.right) > 1:
            return Deep(self.measure, self.left, self.quill, self.right[:-1])
        elif not self.quill.is_Vacant:
            return Deep(self.measure, self.left, self.quill.WithoutPrior(), Digit(self.measure, *self.quill.GetFinal()))
        elif len(self.left) == 1:
            return Single(self.measure, self.left[0])
        else:
            return Deep(self.measure, self.left[0:-1], self.quill, self.left[-1:])
    
    def affix_last(self, new_item):
        if len(self.right) < 4:
            return Deep(self.measure, self.left, self.quill, self.right + Digit(self.measure, new_item))
        else:
            Interchange = Interchange(self.measure, self.right[0], self.right[1], self.right[2])
            return Deep(self.measure, self.left, self.quill.affix_last(Interchange), Digit(self.measure, self.right[3], new_item))
    
    def prepend(self, other):
        return other.append(self)
    
    def append(self, other):
        if not isinstance(other, Deep):
            return other.prepend(self)
        
        return Deep(self.measure, self.left, self._turn_up(self, other), other.right)
    
    def _turn_up(self, left_tree, right_tree):
        
        middle_items = list(left_tree.right) + list(right_tree.left)
        quill = left_tree.quill
        
        while middle_items:
           
            if len(middle_items) == 2 or len(middle_items) == 4:
                quill = quill.affix_last(Interchange(self.measure, middle_items[0], middle_items[1]))
                del middle_items[0:2]
            else:
                quill = quill.affix_last(Interchange(self.measure, middle_items[0], middle_items[1], middle_items[2]))
                del middle_items[0:3]
        return quill.append(right_tree.quill)
    
    def SplitWith(self, predicate, initial_explanation):
        left_explanation = self.measure.Operator(initial_explanation, self.left.explanation)
        quill_explanation = self.measure.Operator(left_explanation, self.quill.explanation)
    
        if predicate(left_explanation):
            left_items, right_items = self.left.Splitting_digit(initial_explanation, predicate)
            return to_tree(self.measure, left_items), ExtensiveLeft(self.measure, right_items, self.quill, self.right)
        elif predicate(quill_explanation):
            left_quill, right_quill = self.quill.Splitting_with(predicate, left_explanation)
            split_Interchange = right_quill.get_elemental()
            right_quill = right_quill.absentElemental()
            before_digit, after_digit = Digit(self.measure, *split_Interchange).Splitting_digit(self.measure.Operator(left_explanation, left_quill.explanation), predicate)

            return ExtensiveRight(self.measure, self.left, left_quill, before_digit), ExtensiveLeft(self.measure, after_digit, right_quill, self.right)
        else:
            left_items, right_items = self.right.Splitting_digit(quill_explanation, predicate)
            return ExtensiveRight(self.measure, self.left, self.quill, left_items), to_tree(self.measure, right_items)
    
    def __repr__(self):
        return  % (self.left, self.quill, self.right)


def ValueIterator(tree):
    while not tree.is_Vacant:
        yield tree.get_elemental()
        tree = tree.absentElemental()


# In[ ]:




