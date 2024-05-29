import p102q


def test_is_origin_inside_triangle():
    assert p102q.is_origin_inside_triangle(((-340, 495), (-153, -910), (835, -947)))
    assert not p102q.is_origin_inside_triangle(((-175, 41), (-421, -714), (574, -645)))


def test_solve():
    triangles1 = [
        ((-340, 495), (-153, -910), (835, -947)),
        ((-175, 41), (-421, -714), (574, -645)),
    ]
    assert 1 == p102q.solve(triangles1)

    triangles2 = [
        ((int(a), int(b)), (int(c), int(d)), (int(e), int(f)))
        for a, b, c, d, e, f in (
            line.split(",") for line in open("./p102/input.txt").readlines()
        )
    ]
    assert 228 == p102q.solve(triangles2)


# triangle = [(-340, 495), (-153, -910), (835, -947)]
# triangle = [(-175, 41), (-421, -714), (574, -645)]
