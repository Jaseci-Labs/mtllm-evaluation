import:py dspy ;
import:py from pydantic, BaseModel, Field ;

with entry {
    llm = dspy.OpenAI(model="gpt-4o");    
    dspy.settings.configure(lm=llm) ;
}

"""Singer."""
class Singer : BaseModel : {
    with entry {
        name: str = Field(description="Name of the Singer");    
        age: int = Field(description="Age");    
        top_songs: list[str] = Field(description="His/Her's Top 2 Songs");
    }
}

"""Get Person Information."""
class GetSinger : dspy.Signature : {
    with entry {
        name: str = dspy.InputField(desc="name of the singer");    
        singer: Singer = dspy.OutputField();
    }
}

with entry {
    bruno_mars = dspy.TypedPredictor(GetSinger)(name="Bruno Mars").singer;    
    print(
        f"{bruno_mars.name}{" is "}{bruno_mars.age}{" years old. His top 2 songs are "}{bruno_mars.top_songs}{"."}"
    ) ;
}

