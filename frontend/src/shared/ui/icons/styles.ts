import styled, { css } from 'styled-components'

type IconProps = {
  color?: string
  width?: string
  height?: string
  clickeable?: string
}

export const Icon = styled.svg<IconProps>`
  ${props => css`
    width: ${props.width};
    height: ${props.height};

    & * {
      fill: ${props.color};
    }

    cursor: ${props.clickeable ? 'pointer' : 'initial'};
  `}
`
