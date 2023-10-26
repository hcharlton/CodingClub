# procedural example without separation of concerns
def print_variant_info(variant: tuple | list) -> None:
    """
    Print information about a variant.

    :param variant: Tuple or list with two elements
    """
    # check if we have an SNP
    bases = ['A', 'T', 'C', 'G', 'N']
    if variant[0] in bases and variant[1] in bases:
        print('This is an SNP')
    else:
        print('This is not an SNP')

    # check if we have a bi-allelic variant
    if variant[0] != variant[1] and variant[0] != 'N' and variant[1] != 'N':
        print('This is a bi-allelic variant')

        # check if we have a transition or transversion
        transitions = [('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')]
        if variant in transitions:
            print('This is a transition')
        else:
            print('This is not a transition')


# TODO: refactor the code above to use a class
class Variant:
    """
    Class to represent a variant.
    """
    #: List of bases
    bases = ['A', 'T', 'C', 'G']

    #: List of transitions
    transitions = [('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')]

    def __init__(self, major: str, minor: str):
        """
        Initialize a Variant with major and minor alleles.

        :param major: Major allele
        :param minor: Minor allele, use 'N' if unknown
        """
        self.major: str = major
        self.minor: str = minor

    def is_transition(self) -> bool:
        """
        Check if the variant is a transition.
        Transitions: A <-> G and C <-> T

        :return: True if it's a transition, False otherwise.
        """
        if self.major in self.transitions and self.minor in self.transitions:
            return True
        else:
            return False

    def is_transversion(self) -> bool:
        """
        Check if the variant is a transversion.
        Transversions are the complementary to transitions.

        :return: True if it's a transversion, False otherwise.
        """
        if not(self.major in self.transitions and self.minor in self.transitions):
            return True
        else:
            return False

    def is_single_base(self, base: str) -> bool:
        """
        Check if a base is a single base.

        :param base: Base to check
        :return: Whether it's a single base or not
        """
        return base in self.bases + ['N']

    def is_snp(self) -> bool:
        """
        Check if the variant is an SNP (Single Nucleotide Polymorphism).

        :return: True if it's an SNP, False otherwise.
        """
        if self.major in self.bases and self.minor in self.bases:
            return True
        else:
            return False

    def is_biallelic(self) -> bool:
        """
        Check if the variant is biallelic.

        :return: True if it's biallelic, False otherwise.
        """
        if self.major != self.minor and self.major != 'N' and self.minor != 'N':
            return True
        else:
            return False



print_variant_info(['A', 'G'])
Variant('A', 'G').print_info()

# assertion transition
variant1 = Variant('A', 'G')
assert variant1.is_transition()
assert not variant1.is_transversion()
assert variant1.is_snp()
assert variant1.is_biallelic()

# assertion transversion
variant2 = Variant('A', 'T')
assert not variant2.is_transition()
assert variant2.is_transversion()
assert variant2.is_snp()
assert variant2.is_biallelic()

# assertion not an SNP
variant3 = Variant('A', 'N')
assert not variant3.is_transition()
assert not variant3.is_transversion()
assert not variant3.is_snp()
assert not variant3.is_biallelic()

# assert monomorphic
variant4 = Variant('A', 'A')
assert not variant4.is_transition()
assert not variant4.is_transversion()
assert variant4.is_snp()
assert not variant4.is_biallelic()

# assert MNP
variant4 = Variant('A', 'CGT')
assert not variant4.is_transition()
assert not variant4.is_transversion()
assert not variant4.is_snp()
assert variant4.is_biallelic()

print("success")