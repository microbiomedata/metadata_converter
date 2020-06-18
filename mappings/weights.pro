% baseline
weight(2.0, [predicate_id='owl:equivalentClass']).

weight(-1, [predicate_id='owl:equivalentClass', subject_category=SC, object_category=OC]) :- freeze(SC-OC,SC\=OC).

% OBO
weight(-3, [predicate_id='owl:equivalentClass', any_match_field='oio:hasNarrowSynonym']).
weight(-3, [predicate_id='owl:equivalentClass', any_match_field='oio:hasBroadSynonym']).
weight(-1, [predicate_id='owl:equivalentClass', any_match_field='oio:hasRelatedSynonym']).

% lexical is lower, stemmming even lower
weight(-1.0, [predicate_id='owl:equivalentClass', match_type=['Lexical','Stemming']]).
weight(-0.5, [predicate_id='owl:equivalentClass', match_type=['Lexical']]).

weight(-1, [match_string=S]) :-  atom_length(S,3).
weight(-2, [match_string=S]) :-  atom_length(S,2).
weight(-3, [match_string=S]) :-  atom_length(S,1).
weight(-99, [match_string=S]) :-  atom_length(S,0).

% reward multi-word terms
weight(W, [match_string=S]) :-  concat_atom(L,' ',S),length(L,Len),W is (Len-1) * 0.3.



