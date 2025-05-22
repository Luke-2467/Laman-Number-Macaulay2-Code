
def distance_polynomials(field,edge):
    '''
    Outputs distance polynomial associated with provided edge for random edge labelling from povided field.
    
    Args:
    field (str): The algebraic field we are working over.
    edge: a list of 2, start and end point of an edge of a graph.

    Returns:
    a string containing distance polynomial
    '''
    M2_code="(x_"+str(edge[0])+"-x_"+str(edge[1])+")^2+(y_"+str(edge[0])+"-y_"+str(edge[1])+")^2-random("+field+")"
    return(M2_code)

def degree_code(G,field="ZZ/101",square_root_minus_1="10"):
    '''
    Outputs Macaulay2 code for computing the ideal defined by provided graph G for generic edge labelling over a field, default being Z/101Z.
    
    Args:
    G (list): A list, first entry a number corresponding to the number of vertices, second entry a list of lists, defining the edges of G.
    field (string): a field, must be in Macaulay2 syntax and input as a string.
    square_root_minus_1 (string): squareroot of minus one over provided field, such a square root must exist.

    Returns:
    a string containing the Macaulay2 code outlined above.
    '''
    #initialise number of vertices and edges from given graph.
    vertices=G[0]
    edges=G[1]
    #begin code string with ring over given field
    M2_code="R="+field+"["
    #add each coordinate for each vertex of G as variable to polynomial,
    #then initiate ideal with 3 polynomials used to ensure no translations or rotations
    for vertex in range(vertices):
        if vertex==vertices-1:
            M2_code=M2_code+"x_"+str(vertex)+",y_"+str(vertex)+"]; I=ideal(x_0,y_0,x_1+"+str(square_root_minus_1)+"*y_1-1,"
        else:
            M2_code=M2_code+"x_"+str(vertex)+",y_"+str(vertex)+","
    #add each edge polynomial to the ideal
    for edge in range(len(edges)):
        if edge==len(edges)-1:
            M2_code=M2_code+distance_polynomials(field,edges[edge])+"); <<degree(I)"
        else:
            M2_code=M2_code+distance_polynomials(field,edges[edge])+","
    print(M2_code)
    return(M2_code)

#G=[2,[[0,1]]]
#degree_code(G, "ZZ/101",10)