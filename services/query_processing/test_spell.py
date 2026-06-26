from services.query_processing.spell_corrector import (
    SpellCorrector
)

corrector = SpellCorrector()

query = "cvoid 15"

print("Original:")
print(query)

print()

print("Corrected:")
print(
    corrector.correct_query(query)
)