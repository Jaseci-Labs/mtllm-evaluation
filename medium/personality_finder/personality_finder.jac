import:py from mtllm.llms, Ollama;

glob llm = Ollama(host="http://52.23.242.52:11343");


enum 'Personality of the Person'
Personality {
   INTROVERT: 'Person who is shy and reticent' = "Introvert",
   EXTROVERT: 'Person who is outgoing and socially confident' = "Extrovert"
}

obj 'Person'
Person {
    has full_name: 'Fullname of the Person': str,
        yod: 'Year of Death': int,
        personality: 'Personality of the Person': Personality;
}

can 'Get Person Information use common knowledge'
get_person_info(name: 'Name of the Person': str) -> 'Person': Person by llm();

with entry {
    # person_obj = get_person_info('Martin Luther King Jr.');
    person_obj = Person(full_name="Martin Luther King Jr." by llm());
    print(f"{person_obj.full_name} was a {person_obj.personality.value} person who died in {person_obj.yod}");
}