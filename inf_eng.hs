-- Structure for a rule, has the number of premises that need to be satisfied
-- and the conclusion that is drawn if they are all satisfied.
-- Conclusions are atomic propositions as are all premises (assumed).
-- We refer to each atomic proposition by an integer and each rule by an integer.


-- although it is quite likely that we need a name rather than a number, as how
-- are we going to know if an atomprop that is fed to infer is in our pretreated
-- structure? Do we assume their names are all numbers? 

data AtomProp   = AtomProp   { name  :: Int
                             , value :: Bool
                             , rules :: [Int]
                             } deriving (Show)

data Rule       = Rule       { premise_count :: Int -- number of (currently) False premises
                             , conclusion    :: Int -- assuming single conc as in spec
                             } deriving (Show)

data PreTreated = PreTreated { rule_list :: [Rule]
                             , atom_list :: [AtomProp]
                             }


infer :: PreTreated -> AtomNames -> SetOfAtomNames
infer [] _  = {}
infer xs {} = foldr 