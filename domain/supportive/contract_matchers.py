from should_dsl import matcher

@matcher
def be_decorated_by():
    '''Checks if the Node is already decorated by a given business decorator '''
    #Substitutes things like decorated.decorators |should| contain(SomeDecorator.__doc__)
    return(lambda candidate, decorator: candidate.decorators.has_key(decorator.__doc__), "%s can %sbe decorated by %s")

