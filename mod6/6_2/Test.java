class Animal {
    private String species;
        public Animal (String species) {
        this.species = species;
    }
    public String getSpecies() {
        return species;
    }
}

class Dog extends Animal {
    private String breed;
    public Dog (String breed) {
        super("Canis lupus familiaris");
        this.breed = breed;
    }
    public String getBreed() {
        return breed;
    }
}

public class Test {
    public static void main(String[] args) {
        Dog myDog = new Dog("Golden Retriever");
        System.out.println("Dog breed: " + myDog.getBreed());
        System.out.println("Dog species: " + myDog.getSpecies());
        // Note: The species is not directly accessible, but it is set in the constructor of Animal.
    }
}